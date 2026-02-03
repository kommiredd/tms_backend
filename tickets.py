from fastapi import APIRouter
from database import tickets
from models import TicketCreate

router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.post("/")
def create_ticket(ticket: TicketCreate, user_id: str):
    tickets.insert_one({
        "title": ticket.title,
        "description": ticket.description,
        "status": "OPEN",
        "created_by": user_id
    })
    return {"message": "Ticket created successfully"}


@router.get("/")
def get_tickets(user_id: str):
    data = list(tickets.find({"created_by": user_id}))
    for t in data:
        t['_id'] = str(t['_id'])
    return data
