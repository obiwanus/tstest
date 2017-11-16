from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes


@permission_classes([])
class FibonacciView(APIView):

    def get(self, request):
        prev_numbers = request.session.get('prev_numbers') or (0, 1)
        next_num = sum(prev_numbers)
        request.session['prev_numbers'] = (prev_numbers[1], next_num)
        return Response(
            {'next_fibonacci_number': next_num},
            status=status.HTTP_200_OK
        )