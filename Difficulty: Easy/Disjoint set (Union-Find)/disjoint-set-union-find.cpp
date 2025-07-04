int find(int par[], int x) {
    if(par[x] == x)
        return x;
        
    return par[x] = find(par, par[x]);
}

void unionSet(int par[], int x, int z) {
    int a = find(par, x);
    int b = find(par, z);
    
    par[a] = b;
        
    return;
}