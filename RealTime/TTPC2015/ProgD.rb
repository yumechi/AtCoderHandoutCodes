require 'prime'

s = gets.chomp

als = {}
for c in s.split("") do
    if c =~ /[[:alpha:]]/ && !als.has_key?(c)
        als[c] = 1
    end
end

lssize = als.size()
if lssize > 5
    p -1
    exit(0)
elsif lssize == 0
    p Prime.prime?(s.to_i) ? s.to_i : -1
    exit(0)
end

nums = ["1", "3", "5", "7", "9"]
for arr in nums.permutation(lssize).to_a do
    ts = Marshal.load(Marshal.dump(s))
    idx = 0
    for k in als.each_key do
        ts.gsub!(k, arr[idx])
        idx += 1
    end
    ts = ts.to_i
    if Prime.prime?(ts)
        p ts
        exit(0)
    end
end

p -1
