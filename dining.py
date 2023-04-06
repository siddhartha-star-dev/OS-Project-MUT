import threading
import time
import networkx as nx
from matplotlib import pyplot as plt

def plot_rag(n):
    G = nx.DiGraph()
    resource_types=[]
    for x in range(n):
        resource_types.append(f"F{x}")
    processes=[]
    for x in range(n):
        processes.append(f"P{x}")
    allocation=[[0 for x in range(n)] for x in range(n)]
    for x in range(0,n):
        allocation[x][x]=1
    request=[[0 for x in range(n)] for x in range(n)]
    for x in range(0,n):
        request[x][(x+n+1)%n]=1
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
    nx.draw(G, pos, with_labels = True, node_size=[700 for x in range(0,2*n)], connectionstyle='arc3, rad = 0.12')
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels,font_size=7)
    plt.show()


def pick_fork(phil_no):
    with forks[phil_no%n]:
        print(f"Philosopher {phil_no%n} picked fork {phil_no%n}\n",flush=True,end="")
        time.sleep(0.5)
        with forks[(phil_no+1)%n]:
            print(f"Philosopher {phil_no%n} picked fork {(phil_no+1)%n}\n",flush=True,end="")
            print("This statement will never be printed because of deadlock")


if __name__ == '__main__':
    print("Simulating dining philosopher problem")
    n=int(input("How many philosophers are there? "))
    forks=[threading.Lock() for x in range(n)]
    threads=[]
    for x in range(n):
        threads.append(threading.Thread(target=pick_fork,args=[x,]))
    for x in range(n):
        threads[x].start()
    
    print("This situation has caused a deadlock")
    print("All philosophers have picked their left fork")

    inp=input("Would you like to analyse the resource allocation graph: ")
    if(inp.lower()=="yes"):
        plot_rag(n)
    else:
        exit(0)
