


(function($) {
  
  var galleryInstance = null;
  
  function Gallery(element, settings) {
    //console.log("new Gallery", element, settings);
    this.element = element;
    this.$element = $(element);
    this.width =  settings.width || this.$element.width();
    this.height =  settings.height || this.$element.height();
    this.queue = [];
    this.images = settings.metadata.map(function(obj) {
      return "/media/" + obj.image;
    });
    this.metaElement = settings.metaElement;
    this.metadata = settings.metadata || null; // optional
    this.delay = settings.delay || 3000;
    this.fadeTime = settings.fadeTime || 2000;
    this.startDate = new Date;
    this.index = 0;
    this.load();
  }
  
  Gallery.prototype = {
    load: function() {
      for (var i=0 ; i<this.images.length ; i++)
      {
        this._loaded = 0;
        
        var img = this._loadImage(this.images[i],i);
        this.queue.push(img);
      }
    },
    
    _loadImage : function(src, index){
      var image = new Image();
      $(image).css({
        display: "none",
        position: "absolute",
        "width" : "auto",
        "height" : "auto",
        "max-width": this.width,
        "max-height": this.height
      }) 
      //console.log("queueing", image);
    
      image.onload = (function () {
        this._loaded++;
        if (this._loaded == 1)
        {
          this.index = index;
          //console.log('loaded first image', image);
          this.$element.append(image);      
        
          this.centerImage($(image));

          $(image).fadeIn('slow');
          if (this.metadata && this.metaElement)
            this.showMeta(this.index);
          
          //console.log('preloading 1 done. kick-off timer for carroussel');
          // kick-off timer for the carroussel
          this._loopTimer = setTimeout(this.loop.bind(this), this.delay);
        }
      
      }).bind(this);
  
      image.src = src;
      return image;
    },
    
    loop: function () {
      this.crossfade(this.fadeTime);
      this._loopTimer = setTimeout(this.loop.bind(this), this.delay + this.fadeTime);
    },
    
    showMeta: function(i) {
      var m = this.metadata[i];
      var $m = $(this.metaElement);
      $m.find(".title").text( m["title"] );
      $m.find(".technique").text( m["technique"] );
      $m.find(".dimensions").text( m["dimensions"] );
    },
    
    crossfade: function (fadetime, inc) {
      //console.log('crossfade');
      inc = inc || 1;
      var $out = $(this.queue[this.index]);
      this.index+=inc;
      this.index %= this.images.length; // wrap at end
      if (this.index < 0) this.index  = this.images.length-1; // wrap at begin
      //console.log("next: ", this.index);
      var $in = $(this.queue[this.index]);
        
      //console.log($out[0], $in[0]); 
      
      $out.fadeOut(fadetime, function () { $out.detach(); });
      $in.appendTo(this.$element).hide().fadeIn(fadetime);
      this.centerImage($in);
      
      // update metadata
      if (this.metadata && this.metaElement)
        setTimeout( (function() { this.showMeta(this.index); }).bind(this), fadetime/2 );
    },
    
    centerImage : function($img) {
      var gw = this.width,
          gh = this.height,
          w = $img.width(),
          h = $img.height();
      
      if (w / h < gw/gh) 
        $img.css({ left: (gw - w) / 2}); // hor centering
      else
        $img.css({ top: (gh - h) / 2}); // vert centering
    },
    
    registerControls: function($controls) {
          this.$prev = $controls.find("[data-role='prev']");
          this.$pause = $controls.find("[data-role='pause']");
          this.$play = $controls.find("[data-role='play']");
          this.$next = $controls.find("[data-role='next']");
          
          this.$prev.click($.proxy(galleryInstance.prev, galleryInstance));
          this.$pause.click($.proxy(galleryInstance.pause, galleryInstance));
          this.$play.click($.proxy(galleryInstance.play, galleryInstance));
          this.$next.click($.proxy(galleryInstance.next, galleryInstance));
    },
    
    prev: function() {
      //console.log("prev");
      this.pause();
      this.crossfade(0, -1);
    },
    
    pause: function() {
      //console.log("pause");
      this.$play.show();
      this.$pause.hide();
      clearTimeout(this._loopTimer);
    },
    
    play: function() {
      //console.log("play");
      this.$play.hide();
      this.$pause.show();
      this.loop()
    },
    
    next: function() {
      //console.log("next");
      this.pause();
      this.crossfade(0);
    }
  };
  
    $.gallery = function(element, options) {

        var defaults = {
            foo: 'bar',
            onFoo: function() {}
        }

        var plugin = this;

        plugin.settings = {}

        var $element = $(element),
             element = element;

        var init = function() {
          var settings = $.extend({}, defaults, options);
          // code goes here
          //console.log(element);
          window.g = galleryInstance = new Gallery(element, settings);
          
          var $controls = $("[data-role='gallery-controls']");
          galleryInstance.registerControls($controls);
        }

        init();

    }

    $.fn.gallery= function(options) {

        return this.each(function() {
            if (undefined == $(this).data('pluginName')) {
                var plugin = new $.gallery(this, options);
                $(this).data('gallery', plugin);
            }
        });

    }

})(jQuery);
