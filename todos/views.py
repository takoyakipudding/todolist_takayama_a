from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Todo
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .forms import SignUpForm, TodoForm
from django.http import JsonResponse
from django.views import View
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST

def update_order(request):
    todo_ids = request.POST.getlist('todo_ids[]')
    # todo_idsに基づいて順序を更新する処理を実装する
    try:
        for index, todo_id in enumerate(todo_ids):
            todo = Todo.objects.get(id=todo_id)
            todo.order = index + 1  # 1から始まる順序にする場合
            todo.save()
        return JsonResponse({'message': 'Order updated successfully'})
    except Todo.DoesNotExist:
        return JsonResponse({'error': 'Todo not found'}, status=404)

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'
    login_url = '/accounts/login/'

    def get_queryset(self):
        queryset = Todo.objects.all().order_by('order')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_date'] = timezone.now()  # 現在の日付を追加
        return context

def add(request):
    title = request.POST['title']
    Todo.objects.create(title=title)

    return redirect('todos:index')

def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('todos:index')

def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    todo.isCompleted = isCompleted

    todo.save()
    return redirect('todos:index')

def edit(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos:index')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/edit.html', {'form': form, 'todo': todo})

def index(request):
    return redirect('/todos')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = '' 
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})