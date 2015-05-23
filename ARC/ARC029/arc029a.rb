n = gets.to_i
li = []
n.times { li.push gets.to_i }
maxnum = 999999
1.upto(2 ** n) { |i|
	t = i
	plateA = 0
	plateB = 0
	0.upto(n - 1) { |j|
		if (t & 1) == 1
			plateA += li[j]
		else
			plateB += li[j]
		end
		t >>= 1
	}
	maxnum = [maxnum, [plateA, plateB].max].min
}
puts maxnum