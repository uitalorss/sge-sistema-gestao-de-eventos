

integrity_error = {
    400:{
        "description": "Integrity Error",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Favor verificar dados."
                } 
            }
        }
    }
}

evento_not_found = {
    404:{
        "description": "Not Found Error",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Evento não encontrado."
                } 
            }
        }
    }
}

post_inscricao_errors = {
    406:{
        "description": "HTTP Exception",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Evento com capacidade esgotada."
                } 
            }
        }
    },
    400:{
        "description": "HTTP Exception",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Usuário já cadastrado em evento."
                } 
            }
        }
    }  
}

delete_inscricao = {
    400:{
        "description": "HTTP Exception",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Inscrição não encontrada."
                } 
            }
        }
    }     
}

login_error = {
    401:{
        "description": "HTTP Exception",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Usuário e/ou senha incorretos."
                } 
            }
        }
    }       
}

organizador_not_found = {
    404:{
        "description": "HTTP Exception",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Organizador não encontrado."
                } 
            }
        }
    }     
}

participante_not_found = {
    404:{
        "description": "HTTP Exception",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Organizador não encontrado."
                } 
            }
        }
    }     
}