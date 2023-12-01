program day1
    implicit none

    integer :: iostat, unit, sum, first, last, num, i
    character(len=256) :: line
    character(len=1) :: ch
    logical :: first_found

    sum = 0
    unit = 10
    iostat = 0

    open(unit= unit, file='input.txt', status='old', action='read', iostat=iostat)
    if (iostat /= 0) then
        print *, 'Error opening file.'
        stop
    endif

    do
        read(unit, '(A)', iostat=iostat) line
        if (iostat /= 0) exit 

        first_found = .false.
        first = 0
        last = 0

        do i = 1, len_trim(line)
            ch = line(i:i)
            if (ichar(ch) >= ichar('0') .and. ichar(ch) <= ichar('9')) then
                read(ch, *) num
                if (.not. first_found) then
                    first = num
                    first_found = .true.
                endif
                last = num
            endif
        end do

        if (first_found) then
            sum = sum + first * 10 + last
        endif
    end do

    close(unit)

    print *, 'Sum:', sum

end program day1