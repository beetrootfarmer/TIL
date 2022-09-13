convert("   tekramngnaad   ") == "DAANGNMARKET" # true
convert("   torrak         ") == "KARROT" # true
convert("   remmus         ") == "SUMMER" # true

def convert(input)
	input.strip
	input.reverse
	input.upcase
end

# ruby class 만들고 메소드 호출하는 방법
class MyClass
    def say_hello
      puts "Hello World"
    end
  end
  
  def another_hello
    puts "Hello World (from a method)"
  end
  
  c = MyClass.new
  c.say_hello
  another_hello