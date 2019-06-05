def two_sum(nums, target)
    hash = {}

    nums.each_with_index do |num,i|
        hash[i] = num
    end

   answer = hash.collect do |key,value|
        wanted  = target-value
        if hash.has_value?(wanted) && hash.key(wanted) != key
            return array=[key,hash.key(wanted)]
            break
        end
    end

    return answer
end
