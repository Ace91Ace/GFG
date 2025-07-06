class Job{
    int id, deadline, profit;
    Job(int id,int deadline,int profit){
        this.id=id;
        this.deadline=deadline;
        this.profit=profit;
    }
}
class Solution {
    public ArrayList<Integer> jobSequencing(int[] deadline, int[] profit) {
        int n=deadline.length;
        Job[] jobs=new Job[n];
        for(int i=0;i<n;i++)jobs[i]=new Job(i+1,deadline[i],profit[i]);
        Arrays.sort(jobs,(a,b)->b.profit-a.profit);
        int max=0;
        for(Job job:jobs)max=Math.max(max,job.deadline);
        int hash[]=new int[max+1];
        Arrays.fill(hash,-1);
        int cnt=0,maxProfit=0;
        for(Job job:jobs){
            for(int j=job.deadline;j>0;j--){
                if(hash[j]==-1){
                    hash[j]=job.id;
                    cnt++;
                    maxProfit+=job.profit;
                    break;
                }
            }
        }
        ArrayList<Integer> res=new ArrayList<>();
        res.add(cnt);
        res.add(maxProfit);
        return res;
        
    }
}