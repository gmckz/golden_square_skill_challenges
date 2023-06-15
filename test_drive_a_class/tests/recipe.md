
Integrated tests:

Initialising diary object and adding a diary entry object returns diary entry object

Add multiple diary entry objects, diary.all reeturns list of instances of diaryentry

add multiple diary objects, diary.countwords returns integer representing number of words in all entries

add multiple diary object, diary.reading time returns number of minutes it would take to read all entries

given multiple diary objects with different length contents, returns instance of diary entry  that is closest to, but not over, the length that the user could read in the minutes they have available given their reading speed.

Unit tests:

initialising diaryentry sets title and contents

count words returns integer of number of words in contents

given wpm reading time returns estimate of reading time in minutes

given wpm, minutes reading chunk returns a chunk of contents that can be read in that time
