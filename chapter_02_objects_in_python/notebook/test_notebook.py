from notebook import Note, Notebook

def test_note_creation_generates_unique_ids():
    note1 = Note("hello first")
    note2 = Note("hello again")
    assert note1.id != note2.id

def test_search_succeeds_when_filter_term_in_memo():
    note = Note("hello first")
    assert note.match("hello") == True

def test_search_fails_when_filter_term_not_in_memo():
    note = Note("hello again")
    assert note.match("second") == False

def pytest_funcarg__notebook_with_one_note(request):
    notebook = Notebook()
    notebook.new_note("hello world")
    return notebook

def pytest_funcarg__notebook_with_two_notes(request):
    notebook = Notebook()
    notebook.new_note("hello world")
    notebook.new_note("hello again")
    return notebook

def test_note_creation_through_notebook_creates_memos_correctly(notebook_with_two_notes):
    assert notebook_with_two_notes.notes[0].memo == "hello world"
    assert notebook_with_two_notes.notes[1].memo == "hello again"

def test_note_search_with_term_in_all_notes_returns_full_all_notes_in_list(notebook_with_two_notes):
    assert notebook_with_two_notes.search("hello") == \
            notebook_with_two_notes.notes

def test_note_search_with_term_in_second_note_returns_second_note_in_list(notebook_with_two_notes):
    assert notebook_with_two_notes.search("again") == \
            [notebook_with_two_notes.notes[1],]

def test_modify_memo_modifies_note_memo(notebook_with_one_note):
    notebook_with_one_note.modify_memo(notebook_with_one_note.notes[0].id,
            "hi world")
    assert notebook_with_one_note.notes[0].memo == "hi world"
