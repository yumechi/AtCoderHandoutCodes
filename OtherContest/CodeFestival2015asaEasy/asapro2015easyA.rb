res = 0
i = gets.to_i
while true do
    t = Math.sqrt(i).to_i
    if t * t == i
        break
    end
    i += 1
    res += 1
end
puts res