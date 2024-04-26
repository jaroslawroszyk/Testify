from django.shortcuts import render, redirect
from ..models import Test, Question, Answer

def create_test_view(request):
    if request.method == 'POST':
        # Retrieve test name from form
        test_name = request.POST.get('test_name')
        # Create a new test
        test = Test.objects.create(name=test_name)
        
        # Process each question and its answers
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_text = value
                question = Question.objects.create(test=test, question_text=question_text)

                # Add answers for this question
                for i in range(1, 5):
                    answer_text = request.POST.get(f'answer_{key.split("_")[1]}_{i}')
                    if answer_text is not None and answer_text.strip():  # Check if answer text is not None and not empty
                        is_correct = request.POST.get(f'is_correct_{key.split("_")[1]}_{i}', False)
                        # Convert is_correct to boolean
                        is_correct = is_correct == 'true'  # Convert to boolean value
                        Answer.objects.create(question=question, answer_text=answer_text, is_correct=is_correct)
        
        # Get the ID of the created test and format it as a 6-digit string
        test_code = str(test.id).zfill(6)
        
    else:
        # Get the ID of the next test to be inserted and format it as a 6-digit string
        next_test_id = Test.objects.latest('id').id + 1
        test_code = str(next_test_id).zfill(6)
    
    # Pass the test code to the template
    return render(request, 'app/create_test.html', {'test_code': test_code})
