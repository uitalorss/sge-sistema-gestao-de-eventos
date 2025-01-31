from fastapi import FastAPI

from api.v1.api import api_router
from core.configs import settings

app = FastAPI(
    title="Sistema de gerenciamento de eventos",
    description="A API de Gerenciamento de Eventos permite a criação, organização e participação em eventos de forma eficiente. Com ela, organizadores podem cadastrar eventos, gerenciar inscrições e acompanhar participantes. Os usuários podem visualizar eventos disponíveis e se inscrever facilmente. A API oferece funcionalidades como autenticação, filtros de pesquisa e notificações, garantindo uma experiência completa para todos os envolvidos..",
    version="0.0.2",
)

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
    )
