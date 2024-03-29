import json
import time
import rsa
import hashlib as hl

def sort_glob(fp):  # Функция для правильного упорядочивания путей к файлам блоков
    easy_glob = sort_glob(fp)
    out = []
    num = 0
    while len(easy_glob) > 0:
        for i, el in enumerate(easy_glob):
            if el[16:-5] == str(num):
                out.append(easy_glob.pop(i))
                num += 1
                break
    return out

def read_transactions(fp):  # Считываем цепочку уже созданных транзакций
    fp_transaction = fp + 'transaction' + '*' + '.json'
    fp_signature = fp + 'signatue' + '*' + '.dat'
    files_transactions = sort_glob(fp_transaction)
    files_signatures = sort_glob(fp_signature)
    if len(files_signatures) == len(files_transactions):
        pass
    else:
        raise Exception('Not all transactions were signed')

    transactions = []
    for i, file_name_transction in enumerate(files_transactions):
        file_name_signatures = files_signatures[i]
        with open(file_name_transction, 'r', encoding='UTF8') as file:
            transactions.append([json.load(file)])
            transactions[-1][0]['user']['public_key'] = rsa.PublicKey(
                transactions[-1][0]['user']['public_key'][0],
                transactions[-1][0]['user']['public_key'][1]
            )
        with open(file_name_signatures, 'rb') as bytes_code:
            transactions[-1].append(bytes_code.read())
    return transactions

def verify(transaction, signature):
    key = transaction['user']['public_key']
    return rsa.verify(message=str(transaction).encode(), signature=signature, pub_key=key)


def read_transactions(fp):  # Считываем цепочку уже созданных транзакций
    fp_transaction = fp + 'transaction' + '*' + '.json'
    fp_signature = fp + 'signatue' + '*' + '.dat'
    files_transactions = sort_glob(fp_transaction)
    files_signatures = sort_glob(fp_signature)
    if len(files_signatures) == len(files_transactions):
        pass
    else:
        raise Exception('Not all transactions were signed')

    transactions = []
    for i, file_name_transction in enumerate(files_transactions):
        file_name_signatures = files_signatures[i]
        with open(file_name_transction, 'r', encoding='UTF8') as file:
            transactions.append([json.load(file)])
            transactions[-1][0]['user']['public_key'] = rsa.PublicKey(
                transactions[-1][0]['user']['public_key'][0],
                transactions[-1][0]['user']['public_key'][1]
            )
        with open(file_name_signatures, 'rb') as bytes_code:
            transactions[-1].append(bytes_code.read())
    return transactions

def mercles_tree(hashs):
    def balancing(hashs):
        if len(hashs) % 2 == 0:
            return hashs

        hashs.append(hashs[-1])
        return hashs

    tmp_hashs = []
    if len(hashs) > 1:
        balance_hashs = balancing(hashs)
        for i in range(0, len(balance_hashs), 2):
            j = (i + 1)
            el1, el2 = hashs[i], hashs[j]
            sum = el1 + el2
            tmp_hashs.append(hl.sha256(sum.encode()).hexdigest())
        return mercles_tree(tmp_hashs)
    return hashs[0]