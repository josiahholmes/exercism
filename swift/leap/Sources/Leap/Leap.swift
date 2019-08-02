//Solution goes in Sources
class Year {
    var year: Int
    var isLeapYear: Bool {
        return (year % 4 == 0) && ((year % 100 != 0) || (year % 400 == 0))
    }

    init(calendarYear: Int) {
        self.year = calendarYear
    }
}
