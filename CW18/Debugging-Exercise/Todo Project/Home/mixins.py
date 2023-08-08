from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.views import View
from django.core.exceptions import PermissionDenied


class TodoMixin(View):
    form_class = TodoForm
    template_name = None

    def dispatch(self, request, *args, **kwargs):
        todo = Todo.objects.get(id=kwargs['pk'])
        if not todo.user == request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        todo = Todo.objects.get(id=kwargs['pk'])
        return render(request, self.template_name, {'todo': todo})

    def post(self, request, pk):
        todo = Todo.objects.get(id=pk)
        form = self.form_class(request.POST, instance=todo)
        if form.is_valid():
            todo.save()
            return redirect('thank_you')
        return render(request, self.template_name, {'todo': todo})
