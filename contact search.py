# -----------------------------
# Contact Search & Deduplication
# -----------------------------

contacts = [
    {"name": "Amina Yusuf", "phone": "08031234567", "email": "amina@gmail.com"},
    {"name": "Yusuf Bello", "phone": "08051239876", "email": "yusuf@yahoo.com"},
    {"name": "amina yusuf", "phone": "08031234567", "email": "amina@yahoo.com"},
    {"name": "Sadiq Musa", "phone": "08123456789", "email": "sadiq@gmail.com"},
    {"name": "Zainab Ali", "phone": "08123456789", "email": "zainab@gmail.com"},
    {"name": "Musa Sadiq", "phone": "09011112222", "email": "sadiq@gmail.com"}
]


# ---- Case-insensitive substring search ----
def search_contacts(query):
    query = query.lower()
    return [
        c for c in contacts
        if query in c["name"].lower()
        or query in c["phone"]
        or query in c["email"].lower()
    ]


# ---- Deduplication by phone OR email ----
def deduplicate_contacts(contact_list):
    seen_phones = set()
    seen_emails = set()

    unique_contacts = []
    removed_log = []

    for c in contact_list:
        phone = c["phone"]
        email = c["email"].lower()

        if phone in seen_phones:
            removed_log.append((c, "Duplicate phone"))
        elif email in seen_emails:
            removed_log.append((c, "Duplicate email"))
        else:
            unique_contacts.append(c)
            seen_phones.add(phone)
            seen_emails.add(email)

    return unique_contacts, removed_log


# ---- CSV output ----
def write_csv(filename, contact_list):
    with open(filename, "w") as f:
        f.write("name,phone,email\n")
        for c in contact_list:
            f.write(f"{c['name']},{c['phone']},{c['email']}\n")


# ---- Log output ----
def write_log(filename, removed):
    with open(filename, "w") as f:
        for contact, reason in removed:
            f.write(f"Removed {contact} | Reason: {reason}\n")


# ---- Run deduplication ----
cleaned_contacts, removed_duplicates = deduplicate_contacts(contacts)

write_csv("cleaned_contacts.csv", cleaned_contacts)
write_log("deduplication_log.txt", removed_duplicates)


# ---- Demo search ----
results = search_contacts("amina")
print("Search results:")
for r in results:
    print(r)

print("\nCleaned contacts written to cleaned_contacts.csv")
print("Duplicate log written to deduplication_log.txt")
