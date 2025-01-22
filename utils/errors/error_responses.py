common_response_evento = {
    400: {
        "description": "Integrity Error",
        "content": {
            "application/json": {
                "example": {"detail": "Favor verificar dados."}
            }
        },
    }
}

common_response = {
    400: {
        "description": "Integrity Error",
        "content": {
            "application/json": {
                "example": {"detail": "Email informado já cadastrado."}
            }
        },
    }
}

auth_responses = {
    401: {
        "description": "Credential Error",
        "content": {
            "application/json": {
                "examples": {
                    "invalid_token": {
                        "value": {
                            "detail": "Token de acesso inválido ou expirado."
                        }
                    },
                    "missing_token": {
                        "value": {
                            "detail": "Token de acesso não fornecido ou não autorizado."
                        }
                    },
                }
            }
        },
    },
}


def generate_not_found_response(resource: str):
    return {
        404: {
            "description": "Not Found Error",
            "content": {
                "application/json": {
                    "example": {"detail": f"{resource} não encontrado."}
                }
            },
        }
    }


inscricao_responses = {
    406: {
        "description": "HTTP Exception",
        "content": {
            "application/json": {
                "example": {"detail": "Evento com capacidade esgotada."}
            }
        },
    },
    400: {
        "description": "HTTP Exception",
        "content": {
            "application/json": {
                "example": {"detail": "Usuário já cadastrado em evento."}
            }
        },
    },
}

not_found_inscricao_response = {
    400: {
        "description": "HTTP Exception",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Inscrição de participante não encontrada.."
                }
            }
        },
    }
}

login_responses = {
    401: {
        "description": "HTTP Exception",
        "content": {
            "application/json": {
                "example": {"detail": "Usuário e/ou senha incorretos."}
            }
        },
    }
}
