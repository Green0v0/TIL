# notion
# 이진탐색트리를 활용한 길찾기 게임
# node_info로 트리를 알아내라
# 레벨로 분리 이후 값을 기준으로 이진 탐색 트리 생성
# 1. 각 노드에 순서를 매긴다.
# 2. 노드의 고유한 레벨값(y좌표)을 찾는다
# 3. 레벨 순서대로 역순 정렬한다. 레벨이 동일한 경우 x좌표가 작은 순서대로 정렬
# 4. 트리에 각 순서값을 삽입한다. 각 레벨에 대해 x값 기준으로 왼쪽, 오른쪽 구분
# 5. 완성된 트리에 대해 전위 순회, 후위 순회

from sys import setrecursionlimit
setrecursionlimit(10**6)

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def makeTree(nodes, levels, curLevel):
    cur = nodes.pop(0)
    root = TreeNode(cur[-1])

    if nodes:
        for i in range(len(nodes)):
            if nodes[i][1] == levels[curLevel + 1]: # 동일한 레벨이면.
                if nodes[i][0] < cur[0]:
                    # recursive(재귀적)하게 진행
                    root.left = makeTree([x for x in nodes if x[0] < cur[0]], levels, curLevel+1)
                else:
                    root.right = makeTree([x for x in nodes if x[0] > cur[0]], levels, curLevel+1)
    return root

preResult = []
def preorder(node):
    # 재귀적으로 호출, base case
    if node is None:
        return
    preorder(node.left)
    preorder(node.right)
    preResult.append(node.val)

postResult = []
def postorder(node):
    if node is None:
        return
    postResult.append(node.val)
    postorder(node.left)
    postorder(node.right)

def solutoin(nodeinfo):
    levels = sorted(list({x[1] for x in nodeinfo}), reverse=True) # 중복되지 않는 레벨, 큰 순서대로
    nodeinfo = [i+[idx+1] for idx, i in enumerate(nodeinfo)]
    nodeinfo = sorted(nodeinfo, key=lambda x:(x[1], -x[0]), reverse=True)

    root = makeTree(nodeinfo, levels, 0)

    # 전위순회, 후위순회
    preorder(root)
    postorder(root)

    return [postResult, preResult]


print(solutoin(nodeinfo))