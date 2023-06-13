from memo.services.utils import get_wallet, get_network
from memo.models import Memo
from rest_framework import status
from memo.models import Wallet, Network


def create_first_memo(wallet: Wallet, network: Network):
    first_memo = 1000000
    memo = Memo.objects.cerate(network=network, wallet=wallet,
                               first_memo=first_memo, last_memo=first_memo, operation=3)
    return memo


def memo_generator(wallet_addr: str, network: str):
    status_ = status.HTTP_400_BAD_REQUEST
    try:
        network_obj = get_network(network)
        if not network_obj:
            memo = 'Network not found!'
            return status_, memo
        wallet_obj = get_wallet(wallet_addr, network_obj)
        if not wallet_obj:
            memo = 'Wallet not found!'
            return status_, memo
        try:
            memo_obj = Memo.objects.get(wallet=wallet_obj, network=network_obj)
            memo = memo_obj.last_memo + memo_obj.operation
            memo_obj.last_memo = memo
            memo_obj.save()
        except Memo.DoesNotExist:
            memo_obj = create_first_memo(wallet_obj, network_obj)
            memo = memo_obj.last_memo
        status_ = status.HTTP_200_OK

    except Exception as e:
        memo = str(e)

    return status_, memo







