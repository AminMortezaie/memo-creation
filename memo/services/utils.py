from memo.models import Wallet, Network


def get_wallet(wallet_address: str, network: Network) -> Wallet | None:
    try:
        wallet_obj = Wallet.objects.filter(address=wallet_address, network=network)
        return wallet_obj
    except Wallet.DoesNotExist:
        pass


def get_network(network: str) -> Network | None:
    try:
        network_obj = Network.objects.get(symbol=network)
    except Network.DoesNotExist:
        try:
            network_obj = Network.objects.get(name=network.capitalize())
        except Network.DoesNotExist:
            network_obj = None
    return network_obj


