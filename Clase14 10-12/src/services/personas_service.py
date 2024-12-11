from src.models.personas_model import (
    insert_persona,
    fetch_all_personas,
    fetch_persona_dynamic,
    update_persona_by_id,
    delete_persona_by_id
)

def add_persona(code, name, price, stock):
    return insert_persona(code, name, price, stock)

def get_all_personas():
    return fetch_all_personas()

def search_persona(condition, parameter):
    return fetch_persona_dynamic(condition, parameter)

def update_persona(id, nombre, edad, ciudad):
    return update_persona_by_id(id, nombre, edad, ciudad)

def delete_persona(id):
    return delete_persona_by_id(id)
