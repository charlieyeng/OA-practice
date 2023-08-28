#Back-end complete function Template for Python 3

'''
    leaves: stores path sum from root to that leaf
    minimum: stores minimum node in the path from root to that leaf
'''
leaves=list()
minimum=list()
'''
    root: current node
    sum: path sum from root to current node
    mini: minimum node in the path from root to leaf
'''
def func(root,s,mini):
    # base case
    # if root is null
    if(root==None):
        return
    # if leaf node
    # store path sum from root to leaf
    # store minimum node in the path from root to leaf
    if(root.left==None and root.right==None):
        leaves.append(s+root.data)
        minimum.append(min(mini,root.data))
        return
    # recur for left and right subtree
    func(root.left,s+root.data,min(mini,root.data))
    func(root.right,s+root.data,min(mini,root.data))
    
def maxRootToLeafPathSum(root):
    global leaves
    global minimum
    leaves=[]
    minimum=[]
    func(root,0,99999999)
    ans=-9999999
    # for each leaf check if the minimum node value is flipped
    # then what is maximum path sum we can get from root to leaf
    for i in range(0,len(leaves)):
        ans=max(ans,max(leaves[i],leaves[i]-2*minimum[i]))
    return ans