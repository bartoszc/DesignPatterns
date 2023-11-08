# Główny obiekt - Document
class Document:
    def __init__(self, content):
        self._content = content

    def display(self):
        return self._content

# Proxy dla Document
class SecureDocumentProxy:
    def __init__(self, document, password):
        self._document = document
        self._password = password

    def display(self, provided_password):
        if provided_password == self._password:
            return self._document.display()
        else:
            return "Błędne hasło. Brak dostępu do dokumentu."

# Testowanie
doc = Document("Tajna zawartość dokumentu")
secure_doc = SecureDocumentProxy(doc, "bezpieczneHaslo")

print(secure_doc.display("zleHaslo"))  # Błędne hasło. Brak dostępu do dokumentu.
print(secure_doc.display("bezpieczneHaslo"))  # Tajna zawartość dokumentu
