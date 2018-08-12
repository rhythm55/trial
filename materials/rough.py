from .models import subtopic
subtopic_id=0
subtopics = subtopic.objects.all()
for i in subtopics:
    if i.id == subtopic_id:
        selected_subtopic = i

print(selected_subtopic)