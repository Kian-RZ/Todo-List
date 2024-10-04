from .models import Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def Create (requests,title):

    try:
        todo = Todo.objects.create(title=title)
    except:
        return Response({'status':'error'})
    todo.save()
    return Response({'status':'ok'})

@api_view(['GET'])
def List (requests):

    res = {}
    todos = Todo.objects.all()
    if todos.count() == 0:
        return Response({'status':'no todo'})
    else:
        for todo in todos:
            res[todo.id] = {'id':todo.id,'title':todo.title,'done':todo.done}
        res['status'] = 'ok'

    return Response(res)

@api_view(['GET'])
def Edit (requests,id,new):

    try:
        obj = Todo.objects.get(id=id)
        obj.title = new
        obj.save()
    except:
        return Response({'status':'error'})    

    return Response({'status':'ok'})

@api_view(['GET'])
def Check (requests,id):
    try:
        obj = Todo.objects.get(id=id)
    except:
        return Response({'status':'error'})
    
    if obj.done != False:
        return Response({'status':'already done'})
    else:
        obj.done = True
        obj.save()

    return Response({'status':'ok'})

@api_view(['GET'])
def Back (requests,id):
    try:
        obj = Todo.objects.get(id=id)
    except:
        return Response({'status':'error'})
    
    if obj.done != True:
        return Response({'status':'already not done'})
    else:
        obj.done = False
        obj.save()

    return Response({'status':'ok'})

@api_view(['GET'])
def Delete (requests,id):

    try:
        obj = Todo.objects.get(id=id)
    except:
        return Response({'status':'error'})
    
    obj.delete()
    
    return Response({'status':'ok'})
