// 03 - Fluent chaining: every mutator returns *this.
//
// Returning a reference to the builder is all it takes to chain calls, so
// configuration reads as a single expression.

#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>

class Person {
 public:
  Person(std::string name, int age, std::string email, bool premium,
         bool newsletter)
      : name_(std::move(name)),
        age_(age),
        email_(std::move(email)),
        premium_(premium),
        newsletter_(newsletter) {}

  void Print() const {
    std::cout << name_ << " (" << age_ << ") <" << email_ << ">"
              << (premium_ ? " [premium]" : "")
              << (newsletter_ ? " [newsletter]" : "") << '\n';
  }

 private:
  std::string name_;
  int age_;
  std::string email_;
  bool premium_;
  bool newsletter_;
};

class PersonBuilder {
 public:
  explicit PersonBuilder(std::string name) : name_(std::move(name)) {}

  // The single line that turns a verbose API into a fluent one: return *this.
  PersonBuilder& WithAge(int age) {
    age_ = age;
    return *this;
  }
  PersonBuilder& WithEmail(std::string email) {
    email_ = std::move(email);
    return *this;
  }
  PersonBuilder& WithPremium(bool premium = true) {
    premium_ = premium;
    return *this;
  }
  PersonBuilder& WithNewsletter(bool on = true) {
    newsletter_ = on;
    return *this;
  }

  Person Build() const {
    if (name_.empty()) throw std::invalid_argument("name is required");
    return Person{name_, age_, email_, premium_, newsletter_};
  }

 private:
  std::string name_;
  int age_ = 0;
  std::string email_;
  bool premium_ = false;
  bool newsletter_ = false;
};

int main() {
  Person ana = PersonBuilder{"Ana"}
                   .WithAge(30)
                   .WithEmail("ana@example.com")
                   .WithPremium()
                   .WithNewsletter()
                   .Build();
  ana.Print();
}
