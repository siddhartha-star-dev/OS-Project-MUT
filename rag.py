import networkx as nx
from matplotlib import pyplot as plt

def plot_rag(resource_types,processes,allocation,request):
    G = nx.DiGraph()
    allocation_edges=[]
    for process_no, allocated in enumerate(allocation):
        for resource_no, allocated_instances in enumerate(allocated):
            if allocated_instances>0:
                G.add_edge(resource_types[resource_no],processes[process_no],weight=allocated_instances)
    request_edges=[]
    for process_no, requested in enumerate(request):
        for resource_no, requested_instances in enumerate(requested):
            if requested_instances>0:
                G.add_edge(processes[process_no],resource_types[resource_no],weight=requested_instances)
    plt.figure(figsize =(18,18))
    pos=nx.spring_layout(G)
    plt.title("Resource allocation graph")
    nx.draw(G, pos, with_labels = True, node_size=[700 for x in range(len(resource_types)+len(processes))], connectionstyle='arc3, rad = 0.12')
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels,font_size=7)
    plt.show()


if __name__ == '__main__':
    r=int(input("Please enter the number of resources: "))
    p=int(input("Please enter the number of processes: "))
    resource_types=[f"R{x+1}" for x in range(r)]
    processes=[f"P{x+1}" for x in range(p)]

    allocation=[]
    for x in range(p):
        row=[int(i) for i in input(f"Enter the resource allocated vector of P{x+1}: ").split()]
        if(len(row)==r):
            allocation.append(row)
        else:
            print("Enter valid vector")
            exit(0)
    request=[]
    for x in range(p):
        row=[int(i) for i in input(f"Enter the request vector of P{x+1}: ").split()]
        if(len(row)==r):
            request.append(row)
        else:
            print("Enter valid vector")
            exit(0)
    plot_rag(resource_types,processes,allocation,request)