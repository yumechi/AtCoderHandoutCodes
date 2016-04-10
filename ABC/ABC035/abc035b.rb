s = gets.chomp
i = gets.to_i

upcount = 0
leftcount = 0
hatena = 0
for c in s.split(//) do
  if c == "L"
    leftcount += 1
  elsif c == "R"
    leftcount -= 1
  elsif c == "U"
    upcount += 1
  elsif c == "D"
    upcount -= 1
  else
    hatena += 1
  end
end

if i == 1
  puts upcount.abs + leftcount.abs + hatena
else
  if hatena >= upcount.abs + leftcount.abs
    puts (hatena - upcount.abs - leftcount.abs) % 2 == 0 ? 0 : 1
  else
    puts (upcount.abs + leftcount.abs - hatena)
  end
end