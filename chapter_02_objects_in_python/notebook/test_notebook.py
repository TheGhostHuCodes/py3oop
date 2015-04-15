from notebook import Note

def test_note_creation_generates_unique_ids():
    note1 = Note("hello first")
    note2 = Note("hello again")
    assert note1.id == 1
    assert note2.id == 2

def test_search_succeeds_when_filter_term_in_memo():
    note = Note("hello first")
    assert note.match("hello") == True

def test_search_fails_when_filter_term_not_in_memo():
    note = Note("hello again")
    assert note.match("second") == False

