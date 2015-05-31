require 'prime'
primes = Prime.each(1000).to_a
res = 1
primes.each { |prim|
	t = prim * res
	if t > 1000
		break
	end
	puts "? " + t.to_s
	STDOUT.flush
	s = gets.chomp 
	while s == "Y"
		t *= prim
		if t > 1000
			break
		end
		puts "? " + t.to_s
		STDOUT.flush
		s = gets.chomp
	end
	res *= t / (prim * res)
}
 
puts "! " + res.to_s