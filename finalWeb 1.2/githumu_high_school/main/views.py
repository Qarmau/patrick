from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import *
from .forms import ContactForm
from django.contrib import messages
from collections import defaultdict
from django.db.models import Q
from django.db.models import Min

def home(request):
    events = Event.objects.all().order_by('-date')[:5]
    news = News.objects.all().order_by('-date')[:5]
    calendar_events = CalendarEvent.objects.all().order_by('date')
    background_images = BackgroundImage.objects.all().order_by('order')
    return render(request, 'home.html', {
        'events': events,
        'news': news,
        'calendar_events': calendar_events, 
        'background_images': background_images,
    })

def about(request):
    about = About.objects.first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Message from {name}',
                message,
                email,
                [about.email],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')
    else:
        form = ContactForm()
    return render(request, 'about.html', {'about': about, 'form': form})
  
 
def administration(request):
    administrators = Administrator.objects.all().order_by('order')
    return render(request, 'administration.html', {'administrators': administrators})

def teaching_staff(request):
    staff = TeachingStaff.objects.all().order_by('order')
    return render(request, 'teaching_staff.html', {'staff': staff})

def achievements(request):
    university_admissions = Achievement.objects.all().order_by('year')
    awards = CoCurricularAward.objects.all().order_by('-year')
    return render(request, 'achievements.html', {
        'university_admissions': university_admissions,
        'awards': awards,
    }) 

def academics(request):
    academics = HolidayAssignment.objects.all().order_by('-date_uploaded')
    
    # Extract unique years
    unique_academics = []
    unique_years = set()
    for assignment in academics:
        if assignment.year not in unique_years:
            unique_academics.append(assignment)
            unique_years.add(assignment.year)
    
    return render(request, 'academics.html', {'academics': unique_academics})

def holiday(request, holiday_id):
    # Retrieve the specific holiday assignment using holiday_id
    holiday = get_object_or_404(HolidayAssignment, id=holiday_id)

    # Retrieve all assignments for the selected year and order them by date uploaded
    all_assignments = HolidayAssignment.objects.filter(year=holiday.year).order_by('-date_uploaded')

    # Dictionary to store unique assignments keyed by title
    unique_assignments = {}
    for assignment in all_assignments:
        if assignment.title not in unique_assignments:
            unique_assignments[assignment.title] = assignment

    # Convert the dictionary values to a list of unique assignments
    filtered_assignments = list(unique_assignments.values())

    return render(request, 'holiday.html', {'holiday': holiday, 'assignments': filtered_assignments})

def grades(request, grade_id):
    # Retrieve the specific assignment using the provided grade_id
    selected_assignment = get_object_or_404(HolidayAssignment, id=grade_id)
    
    # Filter assignments based on the title of the selected assignment
    assignments = HolidayAssignment.objects.filter(title=selected_assignment.title).order_by('-date_uploaded')
    
    # Get all unique grades with their first assignment's id for the selected title
    all_grades = HolidayAssignment.objects.filter(title=selected_assignment.title).values('grade').annotate(first_assignment_id=Min('id'))
    
    return render(request, 'grades.html', {'grades': selected_assignment, 'assignments': assignments, 'all_grades': all_grades})


def years(request,years_id):
    years=HolidayAssignment.objects.get(id=years_id)
    return render(request,'years.html',{'years':years})

def news_detail(request, news_id):
    news = News.objects.get(id=news_id)
    return render(request, 'news_detail.html', {'news': news}) 

def assignments(request, assignment_id):
    # Retrieve the specific assignment using the provided assignment_id
    assignment = get_object_or_404(HolidayAssignment, id=assignment_id)
    
    # Filter assignments based on the same year, grade, and title as the selected assignment
    related_assignments = HolidayAssignment.objects.filter(
        year=assignment.year,
        grade=assignment.grade,
        title=assignment.title
    ).order_by('subject')
    
    return render(request, 'assignments.html', {
        'assignment': assignment,
        'related_assignments': related_assignments,
    })

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = HolidayAssignment.objects.filter(
            Q(title__icontains=query) | 
            Q(grade__icontains=query) |
            Q(subject__icontains=query) | 
            Q(year__icontains=query) | 
            Q(subject__icontains=query) | 
            Q(file__icontains=query)            
        )
    
   
    return render(request, 'search_results.html', {'results': results, 'query': query})


 