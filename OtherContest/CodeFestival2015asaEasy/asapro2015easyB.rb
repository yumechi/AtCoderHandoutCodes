N = gets.to_i
if N  % 2 == 1
    puts -1
    exit(0)
end
inp = gets.chomp
s = inp.split(//)
first, second = s.each_slice(N/2).to_a

res = 0
for i in 0..N/2 do
    if first[i] != second[i]
        res += 1
    end
end
puts res