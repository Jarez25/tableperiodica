from pydantic import BaseModel, Field
from typing import Optional


class Element(BaseModel):
    id: Optional[str] = Field(
        alias="_id", description="Identificador único del elemento")
    atomic_number: int = Field(...,
                               description="Número atómico del elemento", example=1)
    atomic_mass: Optional[float] = Field(
        None, description="Masa atómica en unidades de masa atómica", example=1.008)
    atomic_radius: Optional[float] = Field(
        None, description="Radio atómico en pm", example=53.0)
    block: str = Field(...,
                       description="Bloque al que pertenece el elemento", example="s")
    boiling_point: Optional[float] = Field(
        None, description="Punto de ebullición en Kelvin", example=20.28)
    bonding_type: Optional[str] = Field(
        None, description="Tipo de enlace químico", example="diatomic")
    cpk_hex_color: Optional[str] = Field(
        None, description="Color hexadecimal según el modelo CPK", example="FFFFFF")
    density: Optional[float] = Field(
        None, description="Densidad en g/cm³", example=0.00008988)
    electron_affinity: Optional[float] = Field(
        None, description="Afinidad electrónica en kJ/mol", example=72.769)
    electronegativity: Optional[float] = Field(
        None, description="Electronegatividad según Pauling", example=2.2)
    electronic_configuration: str = Field(
        ..., description="Configuración electrónica", example="1s1")
    group: Optional[int] = Field(
        None, description="Grupo de la tabla periódica", example=1)
    group_block: str = Field(..., description="Bloque de grupo del elemento",
                             example="alkali metal")
    ion_radius: Optional[float] = Field(
        None, description="Radio iónico en pm", example=78.0)
    ionization_energy: Optional[float] = Field(
        None, description="Energía de ionización en kJ/mol", example=1312.0)
    melting_point: Optional[float] = Field(
        None, description="Punto de fusión en Kelvin", example=14.01)
    name: str = Field(..., description="Nombre del elemento",
                      example="Hidrógeno")
    oxidation_states: Optional[str] = Field(
        None, description="Estados de oxidación posibles", example="+1, -1")
    period: int = Field(...,
                        description="Período de la tabla periódica", example=1)
    standard_state: Optional[str] = Field(
        None, description="Estado estándar a 298 K", example="gas")
    symbol: str = Field(..., description="Símbolo del elemento", example="H")
    van_der_waals_radius: Optional[float] = Field(
        None, description="Radio de Van der Waals en pm", example=120.0)
    year_discovered: Optional[str] = Field(
        None, description="Año en que se descubrió el elemento", example="1766")

    class Config:
        allow_population_by_field_name = True
