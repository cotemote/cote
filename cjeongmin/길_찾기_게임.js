const Node = (v) => ({ v, left: null, right: null });

const compareNodeFn = ({ node: a }, { node: b }) => {
    if (a[1] === b[1]) return a[0] - b[0];
    return b[1] - a[1];
};

const insert = (root, nodeinfo) => {
    if (root === null) return Node(nodeinfo);

    if (nodeinfo.node[0] < root.v.node[0]) root.left = insert(root.left, nodeinfo);
    else if (nodeinfo.node[0] > root.v.node[0]) root.right = insert(root.right, nodeinfo);

    return root;
};

const preorder = (root) => {
    if (root === null) return [];
    return [root.v.index].concat(preorder(root.left), preorder(root.right));
};

const postorder = (root) => {
    if (root === null) return [];
    return postorder(root.left).concat(postorder(root.right), [root.v.index]);
};

function solution(nodeinfo) {
    const nodes = nodeinfo.map((node, index) => ({ node, index: index + 1 })).sort(compareNodeFn);

    const root = Node(nodes[0]);

    for (let i = 1; i < nodes.length; i++) insert(root, nodes[i]);

    return [preorder(root), postorder(root)];
}
