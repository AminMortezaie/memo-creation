from rest_framework.views import APIView
from memo.services.memo_generator import memo_generator
from rest_framework.response import Response


class GenerateMemoView(APIView):

    def get(self, request, network, wallet):
        status_, memo = memo_generator(wallet_addr=wallet, network=network)
        return Response(data=str(memo), status=status_)
