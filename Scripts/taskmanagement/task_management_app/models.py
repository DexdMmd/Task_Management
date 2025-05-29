from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()  
    end_time = models.DateTimeField()    
    completed = models.BooleanField(default=False)
    assigned_to = models.CharField(max_length=255, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # New Fields
    status = models.CharField(
        max_length=20,
        choices=[
            ('to_do', 'To Do'),
            ('in_progress', 'In Progress'),
            ('done', 'Done')
        ],
        default='to_do'
    )
    
    category = models.CharField(
        max_length=20,
        choices=[
            ('work', 'Work'),
            ('personal', 'Personal'),
            ('urgent', 'Urgent')
        ],
        default='work'
    )

    def __str__(self):
        return self.title