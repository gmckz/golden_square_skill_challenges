from lib.diary import *
from lib.diary_entry import *

def test_initialise_diaryentry_returns_entry_object():
    my_diary_entry = DiaryEntry("June", "This is my diary entry")
    my_diary = Diary()
    my_diary.add(my_diary_entry)
    assert my_diary_entry in my_diary.entries_list

def test_add_multiple_diary_objs_returns_list_of_instances():
    my_diary_entry = DiaryEntry("June", "This is my diary entry")
    my_diary_entry_2 = DiaryEntry("July", "This is another diary entry")
    my_diary = Diary()
    my_diary.add(my_diary_entry)
    my_diary.add(my_diary_entry_2)
    assert my_diary_entry in my_diary.entries_list
    assert my_diary_entry_2 in my_diary.entries_list

def test_diary_all_returns_list_of_diary_entries():
    my_diary_entry = DiaryEntry("June", "This is my diary entry")
    my_diary_entry_2 = DiaryEntry("July", "This is another diary entry")
    my_diary = Diary()
    my_diary.add(my_diary_entry)
    my_diary.add(my_diary_entry_2)
    assert my_diary.all() == [my_diary_entry, my_diary_entry_2]

def test_diary_count_words_returns_total_word_count():
    my_diary_entry = DiaryEntry("June", "This is my diary entry")
    my_diary_entry_2 = DiaryEntry("July", "This is another diary entry")
    my_diary = Diary()
    my_diary.add(my_diary_entry)
    my_diary.add(my_diary_entry_2)
    assert my_diary.count_words() == 10

def test_diary_reading_time_returns_time_for_all_entries():
    
    my_diary_entry = DiaryEntry("June", "This is my diary entry")
    my_diary_entry_2 = DiaryEntry("July", "This is another diary entry")
    my_diary = Diary()
    my_diary.add(my_diary_entry)
    my_diary.add(my_diary_entry_2)
    assert my_diary.reading_time(2) == 5 

def test_best_entry_returns_closest_length_entry():
    my_diary_entry = DiaryEntry("June", "This is my diary entry " * 2)
    my_diary_entry_2 = DiaryEntry("July", "This is another diary entry")
    my_diary = Diary()
    my_diary.add(my_diary_entry)
    my_diary.add(my_diary_entry_2) 
    assert my_diary.find_best_entry_for_reading_time(2,2) == None
    assert my_diary.find_best_entry_for_reading_time(2,3) == my_diary_entry_2
    assert my_diary.find_best_entry_for_reading_time(2,5) == my_diary_entry


