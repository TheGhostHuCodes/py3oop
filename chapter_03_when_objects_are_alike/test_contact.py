import pytest
from contact import Contact, Supplier

def test_contact_creation_generates_object():
    c = Contact("Some Body", "somebody@example.net")
    assert c.name == "Some Body"
    assert c.email == "somebody@example.net"

def test_supplier_creation_generates_object():
    s = Supplier("Sup Plier", "supplier@example.net")
    assert s.name == "Sup Plier"
    assert s.email == "supplier@example.net"

def test_contact_object_can_not_order():
    with pytest.raises(AttributeError):
        c = Contact("Some Body", "somebody@example.net")
        c.order("I need pliers")

def test_supplier_object_can_order(capsys):
    s = Supplier("Sup Plier", "supplier@example.net")
    s.order("I need pliers")
    out, err = capsys.readouterr()
    assert out == \
            "If this were a real system we would send I need pliers order to" \
            " Sup Plier\n"
