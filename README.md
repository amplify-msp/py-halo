# PyHalo
A simply Python library for the HaloPSA API provided by [Amplify MSP](http://www.amplifymsp.com).

## Requirements
- Python3
- requests

## Usage
- `pip install pyhalo`

```python

# Create a PyHalo object and perform Authentication
pyhalo = PyHalo(
    client_id='client-id',
    client_secret='client-secret',
    domain='amplifymspdev.halopsa.com',
    tenant='amplifymspdev',
    hosted=True,
    scope='all'
)

# Available endpoint groupings are on the pyhalo object
# Actions: pyhalo.actions()
# Agents: pyhalo.agents()
# Appointments: pyhalo.appointments()
# Assets: pyhalo.assets()
# Attachments: pyhalo.attachments()
# Clients: pyhalo.clients()
# Contracts: pyhalo.contracts()
# Invoices: pyhalo.invoices()
# Items: pyhalo.items()
# Knowledge Base: pyhalo.knowledge_base()
# Login Endpoints: pyhalo.login()
# Opportunities: pyhalo.opportunities()
# Quotes: pyhalo.quotes()
# Reports: pyhalo.reports()
# Sites: pyhalo.sites()
# Status: pyhalo.status()
# Suppliers: pyhalo.suppliers()
# Teams: pyhalo.teams()
# Ticket Types: pyhalo.ticket_types()
# Tickets: pyhalo.tickets()
# Users: pyhalo.users()

me_response = pyhalo.agents().get_me()

```
