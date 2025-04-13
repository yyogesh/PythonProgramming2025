contacts = []

def add_contact(name, phone, email):
    """Add a new contact to the list"""
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'id': len(contacts) + 1
    }
    contacts.append(contact)
    return contact

def find_contact(search_term):
    """Find contacts by name or phone number"""
    results = []
    for contact in contacts:
        if (search_term.lower() in contact['name'].lower() or 
            search_term in contact['phone']):
            results.append(contact)
    return results

def update_contact(contact_id, name=None, phone=None, email=None):
    """Update existing contact details"""
    for contact in contacts:
        if contact['id'] == contact_id:
            if name:
                contact['name'] = name
            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email
            return contact
    return None

def list_all_contacts():
    """Return all contacts"""
    return contacts