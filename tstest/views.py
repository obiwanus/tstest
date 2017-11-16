from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes


@permission_classes([])
class FibonacciView(APIView):

    def get(self, request):
        prev_numbers = request.session.get('prev_numbers') or (-1, 1)  # a dirty trick
        next_num = sum(prev_numbers)
        request.session['prev_numbers'] = (prev_numbers[1], next_num)

        return Response(
            {'next_fibonacci_number': next_num},
            status=status.HTTP_200_OK
        )


# Look below for a fancier method of doing the same, not based on session


# def fibonacci_sequence():
#     yield 0
#     yield 1
#     prev = (0, 1)
#     while True:
#         next_fib = sum(prev)
#         yield next_fib
#         prev = (prev[1], next_fib)


# SEQUENCE = fibonacci_sequence()


# @permission_classes([])
# class FibonacciView(APIView):

#     def get(self, request):
#         return Response(
#             {'next_fibonacci_number': next(SEQUENCE)},
#             status=status.HTTP_200_OK
#         )
