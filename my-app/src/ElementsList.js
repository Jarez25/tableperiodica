import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { jsPDF } from "jspdf";  // Importa jsPDF

const ElementsList = () => {
  const [elements, setElements] = useState([]);
  const [loading, setLoading] = useState(true);
  const [group, setGroup] = useState('');
  const [state, setState] = useState('');
  const [atomicNumber, setAtomicNumber] = useState('');

  // Realizar la solicitud con los filtros cada vez que cambian
  useEffect(() => {
    let url = 'http://127.0.0.1:8000/elements/';
    const filters = [];

    if (group) filters.push(`group=${group}`);
    if (state) filters.push(`state=${state}`);
    if (atomicNumber) filters.push(`atomicNumber=${atomicNumber}`);

    if (filters.length > 0) {
      url += `?${filters.join('&')}`;
    }

    // Realiza la solicitud HTTP con los filtros activos
    setLoading(true); // Inicia la carga
    axios.get(url)
      .then((response) => {
        setElements(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error al obtener los elementos:', error);
        setLoading(false);
      });
  }, [group, state, atomicNumber]); // Ejecutar cada vez que los filtros cambian

  const handleFilterChange = (e) => {
    const { name, value } = e.target;
    if (name === 'group') {
      setGroup(value);
    } else if (name === 'state') {
      setState(value);
    } else if (name === 'atomicNumber') {
      setAtomicNumber(value);
    }
  };

  const downloadPDF = () => {
    const doc = new jsPDF();
    doc.text("Lista de Elementos Filtrados", 20, 10);
    let yPosition = 20;

    elements.forEach((element, index) => {
      yPosition += 10;
      doc.text(`${index + 1}. ${element.name} (${element.symbol}) - Grupo: ${element.group}, Estado: ${element.standard_state}, Número Atómico: ${element.atomic_number}`, 20, yPosition);
    });

    doc.save('elements_list.pdf'); // Descarga el archivo PDF
  };

  if (loading) {
    return <div className="text-center py-4">Cargando...</div>;
  }

  return (
    <div className="container mx-auto p-4">
      {/* Título centrado y separador */}
      <h1 className="text-3xl font-bold mb-4 text-center">Lista de Elementos</h1>
      <hr className="border-t-2 border-gray-300 mb-6" /> {/* Línea de separación */}

      {/* Filtros */}
      <div className="mb-6">
        <h2 className="text-xl font-bold mb-4">Filtros</h2>
        <form className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6">
          <input
            type="text"
            name="group"
            value={group}
            onChange={handleFilterChange}
            placeholder="Grupo"
            className="border p-2 rounded"
          />
          <input
            type="text"
            name="state"
            value={state}
            onChange={handleFilterChange}
            placeholder="Estado"
            className="border p-2 rounded"
          />
          <input
            type="number"
            name="atomicNumber"
            value={atomicNumber}
            onChange={handleFilterChange}
            placeholder="Número Atómico"
            className="border p-2 rounded"
          />
        </form>
      </div>

      {/* Botón de descarga */}
      <div className="text-center mb-6">
        <button
          onClick={downloadPDF}
          className="bg-blue-500 text-white px-4 py-2 rounded-lg"
        >
          Descargar PDF
        </button>
      </div>

      {/* Lista de elementos filtrados */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        {elements.map((element) => (
          <div
            key={element._id}
            className="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow duration-300"
            style={{ borderLeft: `8px solid #${element.cpk_hex_color}` }} // Aplicando el color CPK al borde izquierdo de la card
          >
            <div className="flex justify-center items-center mb-4">
              <div className="text-4xl font-bold text-gray-700 mr-4">{element.symbol}</div>
              <div>
                <h2 className="text-2xl font-bold text-gray-800">{element.name}</h2>
                <p className="text-gray-600">Número Atómico: {element.atomic_number}</p>
              </div>
            </div>

            <div className="text-sm text-gray-700">
              <p><strong>Grupo:</strong> {element.group} - <strong>Período:</strong> {element.period}</p>
              <p><strong>Estado Estándar:</strong> {element.standard_state}</p>
              <p><strong>Radio Atómico:</strong> {element.atomic_radius} pm</p>
              <p><strong>Punto de Fusión:</strong> {element.melting_point} °C</p>
              <p><strong>Punto de Ebullición:</strong> {element.boiling_point} °C</p>
              <p><strong>Configuración Electrónica:</strong> {element.electronic_configuration}</p>
              <p><strong>Electronegatividad:</strong> {element.electronegativity}</p>
              <p><strong>Tipo de Enlace:</strong> {element.bonding_type}</p>
              <p><strong>Color CPK:</strong> 
                <span 
                  style={{backgroundColor: `#${element.cpk_hex_color}`}} 
                  className="inline-block w-4 h-4 rounded-full ml-2"
                ></span>
              </p>
              <p><strong>Estados de Oxidación:</strong> {element.oxidation_states}</p>
              <p><strong>Descubierto en:</strong> {element.year_discovered}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ElementsList;
