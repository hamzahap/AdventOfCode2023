program day1
    implicit none

    integer :: iostat, unit, sum, first, last, num, i
    character(len=256) :: line
    character(len=11), dimension(9) :: words
    character(len=11), dimension(9) :: replacements
    character(len=1) :: ch
    logical :: first_found

    data words / 'one        ', 'two        ', 'three      ', &
                 'four       ', 'five       ', 'six        ', &
                 'seven      ', 'eight      ', 'nine       ' /
    data replacements / 'one1one    ', 'two2two    ', 'three3three', &
                         'four4four  ', 'five5five  ', 'six6six    ', &
                         'seven7seven', 'eight8eight', 'nine9nine  ' /

    sum = 0
    unit = 12
    iostat = 0

    open(unit= unit, file='input.txt', status='old', action='read', iostat=iostat)
    if (iostat /= 0) then
        print *, 'Error opening file.'
        stop
    endif

    do
        read(unit, '(A)', iostat=iostat) line
        if (iostat /= 0) exit 

        call convert_words_to_digits(line, words, replacements)

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

subroutine convert_words_to_digits(line, words, replacements)
    implicit none
    character(len=*), intent(inout) :: line
    character(len=11), dimension(9), intent(in) :: words
    character(len=11), dimension(9), intent(in) :: replacements
    integer :: i, j, word_len, line_len, replace_len, k

    line_len = len_trim(line)
    j = 1

    do while (j <= line_len)
        do i = 1, 9
            word_len = len_trim(words(i))
            replace_len = len_trim(replacements(i))
            if (j + word_len - 1 <= line_len) then
                if (line(j:j + word_len - 1) == words(i)) then
                    do k = line_len + replace_len - word_len, j + replace_len, -1
                        line(k:k) = line(k - replace_len + word_len:k - replace_len + word_len)
                    end do
                    line(j:j + replace_len - 1) = replacements(i)
                    line_len = line_len + replace_len - word_len
                    j = j + replace_len - 1
                    exit
                endif
            endif
        end do
        j = j + 1
    end do
end subroutine convert_words_to_digits


