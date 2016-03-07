require 'prime'

s = gets.chomp.to_i
i = 0
if Prime.prime?(s)
	puts "Prime"
else
    if s == 1 or s % 2 == 0 or s % 3 == 0 or s % 5 == 0
        puts "Not Prime"
    else
        puts "Prime"
    end
end
