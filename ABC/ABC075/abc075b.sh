#!/bin/bash

read H W
arr=()
for i in `seq ${H}`; do
    read st
    arr+=($st)
done

range=(-1 0 1)
for i in `seq 0 $((H-1))`; do
    ans=''
    tl=${arr[$i]}
    for j in `seq 0 $((W-1))`; do
        t=${tl:j:1}
        if [ ${t} = '#' ]; then 
            ans=${ans}'#'
            continue
        fi

        cnt=0
        for k in ${range[@]}; do
            if [ $((i+k)) -lt 0 ] || [ $((i+k)) -ge ${H} ]; then
                continue
            fi
            al=${arr[$((i+k))]}
            for l in ${range[@]}; do
                if [ $((j+l)) -lt 0 ] || [ $((j+l)) -ge ${W} ]; then
                    continue
                fi
                a=${al:$((j+l)):1}
                if [[ ${a} = '#' ]]; then
                    let cnt++
                fi
            done
        done
        ans=${ans}${cnt}
    done
    echo ${ans} 
done
