
from math import sqrt, sin, cos
import sys

INF = float( 'inf' )
NaN = float( 'nan' )
EPS = 1e-8

def iterable( obj ):
  try:
    iter( obj )
    return True
  except:
    return False

class repeat:
  ''' repeat( value ) -> ( value, value, value, ... ) '''
  def __init__( self, value ):
    self.value = value
  def __getitem__( self, index ):
    return self.value
  def __iter__( self ):
    while True:
      yield self.value
  def __len__( self ):
    return INF
  def __eq__( self, other ):
    return isinstance( other, repeat ) and self.value == other.value
  def __lt__( self, other ):
    if isinstance( other, repeat ):
      return self.value < other.value
    elif iterable( other ):
      for s, o in zip( self, other ):
        if s < o:
          return True
        elif o < s:
          return False
      return False
    else:
      return NotImplemented
  def __gt__( self, other ):
    if isinstance( other, repeat ):
      return self.value > other.value
    elif iterable( other ):
      for s, o in zip( self, other ):
        if s > o:
          return True
        elif o > s:
          return False
      return True
    else:
      return NotImplemented
  def __le__( self, other ):
    return not self > other
  def __ge__( self, other ):
    return not self < other

def norm( obj ):
  return obj.__abs__()

class Vec( tuple ):
  ''' Vec( x1, x2, ... ) -> Vec '''
  def __new__( cls, *xs ):
    if len( xs ) == 1 and not iterable( xs[ 0 ] ):
      raise TypeError( 'can\'t make a Vec contains only 1 item' )
    elif len( xs ) == 1 and iterable( xs ):
      return tuple.__new__( cls, xs[ 0 ] )
    else:
      return tuple.__new__( cls, xs )
  def __pos__( self, other ):
    return Vec( self )
  def __neg__( self, other ):
    return Vec( -x for x in self )
  def __add__( self, other ):
    return Vec( x + y for x, y in zip( self, other ) )
  def __radd__( self, other ):
    return Vec( y + x for x, y in zip( self, other ) )
  def __sub__( self, other ):
    return Vec( x - y for x, y in zip( self, other ) )
  def __rsub__( self, other ):
    return Vec( y - x for x, y in zip( self, other ) )
  def multiply( self, other ):
    return Vec( x * other for x in self )
  def __mul__( self, other ):
    if isinstance( other, Vec ):
      raise TypeError( 'can\'t multiply Vec and Vec -- use Vec.multiply()' )
    return self.multiply( other )
  def __rmul__( self, other ):
    return Vec( other * x for x in self )
  def __div__( self, other ):
    return Vec( x / other for x in self )
  def __truediv__( self, other ):
    return Vec( x.__truediv__( other ) for x in self )
  def __floordiv__( self, other ):
    return Vec( x // other for x in self )
  def __norm__( self ):
    return sum(x ** 2 for x in self)
  def __abs__( self ):
    return sqrt(self.__norm__())

def unit2d( *args ):
  if len( args ) == 1 and isinstance( args[ 0 ], numbers.Number ):
    return Vec( cos( angle ), sin( angle ) )
  elif len( args ) == 1 and isinstance( args[ 0 ], Vec ):
    return args[ 0 ] / abs( args[ 0 ] )
  elif len( args ) == 1:
    raise TypeError( 'unit2d() can\'t receive %s object' % typename( args[ 0 ] ) )
  else:
    raise TypeError( 'unit2d() requires only 1 argument(s)' )
def dot( va, vb ):
  return sum( xa * xb for xa, xb in zip( va, vb ) )
def dot2d( va, vb ):
  return dot( va, vb )
def cross2d( va, vb ):
  return va[ 0 ] * vb[ 1 ] - va[ 1 ] * vb[ 0 ]
def cross3d( va, vb ):
  return Vec( va[ 1 ] * vb[ 2 ] - va[ 2 ] * vb[ 1 ],
              va[ 2 ] * vb[ 0 ] - va[ 0 ] * vb[ 2 ],
              va[ 0 ] * vb[ 1 ] - va[ 1 ] * vb[ 0 ] )
def rotate2d( self, angle ):
  s, c = sin( angle ), cos( angle )
  return Vec( c * self[ 0 ] - s * self[ 1 ],
              s * self[ 0 ] + c * self[ 1 ] )

class area:
  'area([start, ]stop[, step]) -> area object'
  def __init__( self, *args ):
    if len( args ) == 0:
      raise TypeError( 'area() takes at least 1 arguments (%d given)' % len( args ) )
    elif len( args ) == 1:
      # area( ( x, y ) ) => ( 0, 0 ), ( 1, 0 ), ..., ( x - 1, 0 ), ( 0, 1 ), ..., ( x - 1, y - 1 )
      self.topleft = repeat( 0 )
      self.bottomright = args[ 0 ]
      self.diff = repeat( 1 )
      self.demention = len( args[ 0 ] )
    elif len( args ) == 2:
      # area( ( x1, y1 ), ( x2, y2 ) ) => ( x1, y1 ), ( x1 + 1, y1 ), ..., ( x2 - 1, y1 ), ( x1, y1 + 1 ), ..., ( x2 - 1, y2 - 1 )
      self.topleft = args[ 0 ]
      self.bottomright = args[ 1 ]
      self.diff = repeat( 1 )
      self.demention = len( args[ 0 ] )
      assert len( args[ 1 ] ) == self.demention
    elif len( args ) == 3:
      # area( ( x1, y1 ), ( x2, y2 ), ( x3, y3 ) ) => ( x1, y1 ), ( x1 + x3, y1 ), ..., ( x1, y1 + y3 ), ...
      self.topleft = args[ 0 ]
      self.bottomright = args[ 1 ]
      self.diff = args[ 2 ]
      self.demention = len( args[ 0 ] )
      assert len( args[ 1 ] ) == self.demention
      assert len( args[ 2 ] ) == self.demention
    else:
      raise TypeError( 'area() takes at most 3 arguments (%d given)' % len( args ) )
  def __contains__( self, v ):
    assert len( v ) == self.demention
    return all( x in range( s, e, d ) for x, s, e, d in
                zip( v, self.topleft, self.bottomright, self.diff ) )
  def __iter__( self ):
    return self._items( tuple( zip( self.topleft, self.bottomright, self.diff ) ) )
  def _items( self, rngs ):
    if not rngs:
      yield ()
      return
    for i in range( *rngs[ -1 ] ):
      for r in self._items( rngs[: -1 ] ):
        yield r + ( i, )
