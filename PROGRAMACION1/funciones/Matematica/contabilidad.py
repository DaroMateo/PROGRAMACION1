def calcularprecioconiva(valorsiniva, iva=21):
    """
    Calcula el precio con IVA (Impuesto al Valor Agregado) aplicado
    Args:
        valorsiniva (float): El precio sin IVA.
        iva (int): El porcentaje del IVA. El valor predeterminado es 21.
    Returns:
        float: TEl precio con IVA aplicado.
    """
    #documentacion
    resultado= valorsiniva * (1+(iva/100))
    return resultado

