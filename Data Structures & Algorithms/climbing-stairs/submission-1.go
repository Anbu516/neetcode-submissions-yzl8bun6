func climbStairs(n int) int {
    i:=1
	j:=1

	for k:=0;k<n-1;k++{
		temp:=i
		i+=j
		j=temp
	}

	return i
}